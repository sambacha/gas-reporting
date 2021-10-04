import axios, { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
  baseURL: 'https://api.opensea.io/api/v1',
  timeout: 30000, // 30 secs
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export async function apiGetAccountCollectibles(address: string) {
  const url = `/assets/?owner=${address}`;
  const { data } = await api.get(url);
  return data;
}
