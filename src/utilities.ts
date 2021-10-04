import utf8 from 'utf8';
import { IChainData, IPartialRpcRequest, IJsonRpcRequest } from './types';
import { isNumber } from './bignumber';
import config from './config';
import supportedChains from './chains';

export const debounceRequest = (
  request: Function,
  params: Array<any>,
  timeout: number,
): Promise<any> => {
  return new Promise((resolve, reject) =>
    setTimeout(
      () =>
        request(...params)
          .then((res: any) => resolve(res))
          .catch((err: Error) => reject(err)),
      timeout,
    ),
  );
};

export const capitalize = (value: string): string =>
  value
    .split(' ')
    .map(
      (word: string): string =>
        word.charAt(0).toUpperCase() + word.slice(1).toLowerCase(),
    )
    .join(' ');

export const padLeft = (n: string, length: number, z?: string): string => {
  z = z || '0';
  n = n + '';
  return n.length >= length ? n : new Array(length - n.length + 1).join(z) + n;
};

export const padRight = (n: string, length: number, z?: string): string => {
  z = z || '0';
  n = n + '';
  return n.length >= length ? n : n + new Array(length - n.length + 1).join(z);
};

export const getDataString = (func: string, arrVals: Array<any>): string => {
  let val = '';
  for (let i = 0; i < arrVals.length; i++) val += padLeft(arrVals[i], 64);
  const data = func + val;
  return data;
};

export const getNakedAddress = (address: string): string =>
  address.toLowerCase().replace('0x', '');

export const removeHexPrefix = (hex: string): string =>
  hex.toLowerCase().replace('0x', '');

export const sanitizeHex = (hex: string): string => {
  hex = hex.substring(0, 2) === '0x' ? hex.substring(2) : hex;
  if (hex === '') return '';
  hex = hex.length % 2 !== 0 ? '0' + hex : hex;
  return '0x' + hex;
};

export function getChainData(
  chainId: number,
  noInfuraKeys?: boolean,
): IChainData {
  const chainData = supportedChains.filter(
    (chain: any) => chain.chain_id === chainId,
  )[0];

  if (!chainData) {
    throw new Error('ChainId missing or not supported');
  }

  if (!noInfuraKeys) {
    const INFURA_ID = config.infura.id;

    if (
      INFURA_ID &&
      chainData.rpc_url.includes('infura.io') &&
      chainData.rpc_url.includes('INFURA_ID')
    ) {
      chainData.rpc_url = chainData.rpc_url.replace('INFURA_ID', INFURA_ID);
    }
  }

  return chainData;
}

export function payloadId(): number {
  const datePart: number = new Date().getTime() * Math.pow(10, 3);
  const extraPart: number = Math.floor(Math.random() * Math.pow(10, 3));
  const id: number = datePart + extraPart;
  return id;
}

export const isHexStrict = (hex: string) => {
  return (
    (typeof hex === 'string' || isNumber(hex)) && /^(-)?0x[0-9a-f]*$/i.test(hex)
  );
};

export const hexToUtf8 = (hex: string): string => {
  if (!isHexStrict(hex)) {
    throw new Error(`The parameter "${hex}" must be a valid HEX string.`);
  }

  let str = '';
  let code = 0;
  hex = hex.replace(/^0x/i, '');

  // remove 00 padding from either side
  hex = hex.replace(/^(?:00)*/, '');
  hex = hex.split('').reverse().join('');
  hex = hex.replace(/^(?:00)*/, '');
  hex = hex.split('').reverse().join('');

  const l = hex.length;

  for (let i = 0; i < l; i += 2) {
    code = parseInt(hex.substr(i, 2), 16);
    // if (code !== 0) {
    str += String.fromCharCode(code);
    // }
  }

  return utf8.decode(str);
};

export function formatRequest(request: IPartialRpcRequest): IJsonRpcRequest {
  const formattedRequest: IJsonRpcRequest = {
    id: payloadId(),
    jsonrpc: '2.0',
    ...request,
  };
  return formattedRequest;
}

export function isSuccessful(response: any) {
  return response.data && response.data.status !== '0';
}
