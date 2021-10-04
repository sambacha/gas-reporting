import axios, { AxiosInstance } from 'axios';
import { IGasPrices, IGasGuzzlerRaw, IGasGuzzler } from './types';
import {
  convertStringToNumber,
  divide,
  multiply,
  formatFixedDecimals,
} from './bignumber';

const api: AxiosInstance = axios.create({
  baseURL: 'https://ethgasstation.info/',
  timeout: 30000, // 30 secs
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export const apiGetGasPrices = async (): Promise<IGasPrices> => {
  const { data } = await api.get(`/json/ethgasAPI.json`);
  const result: IGasPrices = {
    timestamp: Date.now(),
    slow: {
      time: convertStringToNumber(multiply(data.safeLowWait, 60)),
      price: convertStringToNumber(divide(data.safeLow, 10)),
    },
    average: {
      time: convertStringToNumber(multiply(data.avgWait, 60)),
      price: convertStringToNumber(divide(data.average, 10)),
    },
    fast: {
      time: convertStringToNumber(multiply(data.fastestWait, 60)),
      price: convertStringToNumber(divide(data.fastest, 10)),
    },
  };
  return result;
};

export const apiGetGasGuzzlers = async (): Promise<IGasGuzzler[]> => {
  const { data } = await api.get(`/json/gasguzz.json`);
  const result = data.map((guzzlerRaw: IGasGuzzlerRaw) => ({
    address: guzzlerRaw.to_address,
    pct: convertStringToNumber(formatFixedDecimals(`${guzzlerRaw.pcttot}`, 2)),
    gasused: convertStringToNumber(guzzlerRaw.gasused),
    id: guzzlerRaw.ID,
  }));
  return result;
};
