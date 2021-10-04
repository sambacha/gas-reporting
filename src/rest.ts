import { RequestGenericInterface } from 'fastify';

export interface RequestWithAddressQuerystring extends RequestGenericInterface {
  Querystring: {
    address: string;
  };
}

export interface RequestWithChainIdQuerystring extends RequestGenericInterface {
  Querystring: {
    chainId: string;
  };
}

export interface RequestWithContractQuerystring
  extends RequestGenericInterface {
  Querystring: {
    contractAddress: string;
  };
}

export interface RequestWithDataQuerystring extends RequestGenericInterface {
  Querystring: {
    data: string;
  };
}

export interface RequestWithFiatQueryString extends RequestGenericInterface {
  Querystring: {
    fiat: string;
  };
}

export interface RequestWithJsonRpcBody extends RequestGenericInterface {
  Body: {
    id: number;
    jsonrpc: string;
    method: string;
    params: any;
  };
}
export type GetAccountBalanceRequest = RequestWithChainIdQuerystring &
  RequestWithAddressQuerystring;

export type GetAccountAssetsRequest = RequestWithChainIdQuerystring &
  RequestWithAddressQuerystring;

export type GetAccountTransactionsRequest = RequestWithChainIdQuerystring &
  RequestWithAddressQuerystring;

export type GetAccountNonceRequest = RequestWithChainIdQuerystring &
  RequestWithAddressQuerystring;

export type GetAccountCollectiblesRequest = RequestWithChainIdQuerystring &
  RequestWithAddressQuerystring;

export type GetTokenBalanceRequest = RequestWithChainIdQuerystring &
  RequestWithAddressQuerystring &
  RequestWithContractQuerystring;

export type GetGasLimitRequest = RequestWithChainIdQuerystring &
  RequestWithContractQuerystring &
  RequestWithDataQuerystring;

export type GetAssetPricesRequest = RequestWithFiatQueryString;

export type GetBlockNumberRequest = RequestWithChainIdQuerystring;

export type GetChainDataRequest = RequestWithChainIdQuerystring;

export type PostRpcRequest = RequestWithJsonRpcBody &
  RequestWithChainIdQuerystring;
