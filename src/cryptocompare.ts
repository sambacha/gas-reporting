import axios, { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
  baseURL: 'https://min-api.cryptocompare.com',
  timeout: 30000, // 30 secs
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export async function apiGetEthPrices(fiat: string) {
  const url = `/data/price?fsym=ETH&tsyms=${fiat}`;
  const { data } = await api.get(url);
  return data;
}

export async function apiGetDaiPrices(fiat: string) {
  const url = `/data/price?fsym=DAI&tsyms=${fiat}`;
  const { data } = await api.get(url);
  return data;
}
