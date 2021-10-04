import axios, { AxiosResponse } from 'axios';
import { IPartialRpcRequest, IJsonRpcRequest } from './types';
import { getChainData, payloadId, formatRequest } from './utilities';
import { convertHexToString, convertStringToNumber } from './bignumber';

export const rpcGetAccountBalance = async (
  address: string,
  chainId: number,
): Promise<number> => {
  const rpcUrl = getChainData(chainId).rpc_url;

  if (!rpcUrl && typeof rpcUrl !== 'string') {
    throw new Error('Invalid or missing rpc url');
  }

  const response = await axios.post(rpcUrl, {
    jsonrpc: '2.0',
    id: payloadId(),
    method: 'eth_getBalance',
    params: [address, 'latest'],
  });

  const balance = convertStringToNumber(
    convertHexToString(response.data.result),
  );
  return balance;
};

export const rpcGetAccountNonce = async (
  address: string,
  chainId: number,
): Promise<number> => {
  const rpcUrl = getChainData(chainId).rpc_url;

  if (!rpcUrl && typeof rpcUrl !== 'string') {
    throw new Error('Invalid or missing rpc url');
  }

  const response = await axios.post(rpcUrl, {
    jsonrpc: '2.0',
    id: payloadId(),
    method: 'eth_getTransactionCount',
    params: [address, 'pending'],
  });

  const nonce = convertStringToNumber(convertHexToString(response.data.result));
  return nonce;
};

export const rpcGetGasLimit = async (
  contractAddress: string,
  data: string,
): Promise<number> => {
  const chainId = 1;

  const rpcUrl = getChainData(chainId).rpc_url;

  const response = await axios.post(rpcUrl, {
    jsonrpc: '2.0',
    id: payloadId(),
    method: 'eth_estimateGas',
    params: [
      {
        to: contractAddress,
        data,
      },
    ],
  });
  const gasLimit = convertStringToNumber(
    convertHexToString(response.data.result),
  );
  return gasLimit;
};

export const rpcGetBlockNumber = async (chainId: number): Promise<number> => {
  const rpcUrl = getChainData(chainId).rpc_url;

  if (!rpcUrl && typeof rpcUrl !== 'string') {
    throw new Error('Invalid or missing rpc url');
  }

  const response = await axios.post(rpcUrl, {
    jsonrpc: '2.0',
    id: payloadId(),
    method: 'eth_blockNumber',
    params: [],
  });
  const blockNumber = convertStringToNumber(
    convertHexToString(response.data.result),
  );
  return blockNumber;
};

export const rpcPostCustomRequest = async (
  chainId: number,
  customRpc: IPartialRpcRequest,
): Promise<any> => {
  const rpcUrl = getChainData(chainId).rpc_url;

  if (!rpcUrl && typeof rpcUrl !== 'string') {
    throw new Error('Invalid or missing rpc url');
  }

  const rpcRequest = formatRequest(customRpc);

  const response = await axios.post(rpcUrl, rpcRequest);

  return response.data.result;
};

export const rpcPostRequest = async (
  chainId: number,
  rpcRequest: IJsonRpcRequest,
): Promise<AxiosResponse> => {
  const rpcUrl = getChainData(chainId).rpc_url;

  if (!rpcUrl && typeof rpcUrl !== 'string') {
    throw new Error('Invalid or missing rpc url');
  }

  const response = await axios.post(rpcUrl, rpcRequest);

  return response;
};
