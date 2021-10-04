import axios, { AxiosInstance } from 'axios';
import {
  IAssetData,
  IBlockScoutTx,
  IBlockScoutTokenTx,
  IParsedTx,
  ITxOperation,
} from './types';
import { multiply, isNumber, convertStringToNumber } from './bignumber';
import { getChainData, isSuccessful } from './utilities';
import { lookupMethod } from './method-registry';
import { rpcGetAccountBalance } from './rpc';

const api: AxiosInstance = axios.create({
  baseURL: 'https://blockscout.com/',
  timeout: 30000, // 30 secs
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

const fetchAndParseTokenBalance = async (
  token: IAssetData,
  address: string,
  chainId: number,
): Promise<IAssetData> => {
  let tokenBalance = '0';
  try {
    const tokenBalanceRes = await apiGetAccountTokenBalance(
      address,
      chainId,
      token.contractAddress,
    );
    if (isSuccessful(tokenBalanceRes)) {
      tokenBalanceRes.data.result;
    }
  } catch (e) {
    // ignore error
  }

  if (
    tokenBalance &&
    isNumber(tokenBalance) &&
    convertStringToNumber(tokenBalance)
  ) {
    token.balance = tokenBalance;
  }

  return token;
};

export async function apiGetAccountBalance(address: string, chainId: number) {
  const chainData = getChainData(chainId);
  const chain = chainData.chain.toLowerCase();
  const network = chainData.network.toLowerCase();
  const module = 'account';
  const action = 'balance';
  const url = `/${chain}/${network}/api?module=${module}&action=${action}&address=${address}`;
  const result = await api.get(url);
  return result;
}

export async function apiGetAccountNativeCurrency(
  address: string,
  chainId: number,
) {
  const chainData = getChainData(chainId);

  const nativeCurrency = chainData.native_currency;

  let nativeBalance = 0;
  try {
    const balanceRes = await apiGetAccountBalance(address, chainId);
    if (isSuccessful(balanceRes)) {
      nativeBalance = balanceRes.data.result;
    }
  } catch (e) {
    // ignore error
  }

  if (!nativeBalance) {
    nativeBalance = await rpcGetAccountBalance(address, chainId);
  }

  nativeCurrency.balance = `${nativeBalance}`;

  return nativeCurrency;
}

export async function apiGetTokenInfo(
  contractAddress: string,
  chainId: number,
) {
  const chainData = getChainData(chainId);
  const chain = chainData.chain.toLowerCase();
  const network = chainData.network.toLowerCase();
  const module = 'token';
  const action = 'getToken';
  const url = `/${chain}/${network}/api?module=${module}&action=${action}&contractaddress=${contractAddress}`;
  const result = await api.get(url);
  return result;
}

export async function apiGetAccountTokenList(address: string, chainId: number) {
  const chainData = getChainData(chainId);
  const chain = chainData.chain.toLowerCase();
  const network = chainData.network.toLowerCase();
  const module = 'account';
  const action = 'tokenlist';
  const url = `/${chain}/${network}/api?module=${module}&action=${action}&address=${address}`;
  const result = await api.get(url);
  return result;
}

export async function apiGetAccountTokenBalance(
  address: string,
  chainId: number,
  contractAddress: string,
) {
  const chainData = getChainData(chainId);
  const chain = chainData.chain.toLowerCase();
  const network = chainData.network.toLowerCase();
  const module = 'account';
  const action = 'tokenbalance';
  const url = `/${chain}/${network}/api?module=${module}&action=${action}&contractaddress=${contractAddress}&address=${address}`;
  const result = await api.get(url);
  return result;
}

export async function apiGetAccountTokenAsset(
  address: string,
  chainId: number,
  contractAddress: string,
) {
  let tokenInfo: any = null;
  try {
    const tokenInfoRes = await apiGetTokenInfo(contractAddress, chainId);
    if (isSuccessful(tokenInfoRes)) {
      tokenInfoRes.data.result;
    }
  } catch (e) {
    // ignore error
  }

  if (tokenInfo) {
    let token: IAssetData = {
      symbol: tokenInfo.symbol,
      name: tokenInfo.name,
      decimals: tokenInfo.decimals,
      contractAddress: tokenInfo.contractAddress,
      balance: '',
    };

    token = await fetchAndParseTokenBalance(token, address, chainId);

    return token;
  } else {
    throw new Error('Could not find token information');
  }
}

export async function apiGetAccountAssets(
  address: string,
  chainId: number,
): Promise<IAssetData[]> {
  const nativeCurrency = await apiGetAccountNativeCurrency(address, chainId);

  let tokenList: IAssetData[] = [];
  try {
    const tokenListRes = await apiGetAccountTokenList(address, chainId);
    if (isSuccessful(tokenListRes)) {
      tokenListRes.data.result;
    }
  } catch (e) {
    // ignore error
  }

  let tokens: IAssetData[] = await Promise.all(
    tokenList.map((token: IAssetData) =>
      fetchAndParseTokenBalance(token, address, chainId),
    ),
  );
  tokens = tokens.filter(
    (token) =>
      !!Number(token.balance) &&
      !!token.balance &&
      !!token.decimals &&
      !!token.name,
  );

  const assets: IAssetData[] = [nativeCurrency, ...tokens];

  return assets;
}

export async function apiGetAccountTxList(address: string, chainId: number) {
  const chainData = getChainData(chainId);
  const chain = chainData.chain.toLowerCase();
  const network = chainData.network.toLowerCase();
  const module = 'account';
  const action = 'txlist';
  const url = `/${chain}/${network}/api?module=${module}&action=${action}&address=${address}`;
  const result = await api.get(url);
  return result;
}

export async function apiGetAccountTokenTx(address: string, chainId: number) {
  const chainData = getChainData(chainId);
  const chain = chainData.chain.toLowerCase();
  const network = chainData.network.toLowerCase();
  const module = 'account';
  const action = 'tokentx';
  const url = `/${chain}/${network}/api?module=${module}&action=${action}&address=${address}`;
  const result = await api.get(url);
  return result;
}

export async function apiGetAccountTransactions(
  address: string,
  chainId: number,
): Promise<IParsedTx[]> {
  let txList: IBlockScoutTx[] = [];
  try {
    const txListRes = await apiGetAccountTxList(address, chainId);
    if (isSuccessful(txListRes)) {
      txList = txListRes.data.result;
    }
  } catch (e) {
    // ignore
  }

  const transactions: IParsedTx[] = txList.map(
    (tx: IBlockScoutTx): IParsedTx => {
      const asset: IAssetData = {
        symbol: 'ETH',
        name: 'Ethereum',
        decimals: '18',
        contractAddress: '',
      };

      const parsedTx: IParsedTx = {
        timestamp: multiply(tx.timeStamp, 1000),
        hash: tx.hash,
        from: tx.from,
        to: tx.to,
        nonce: tx.nonce,
        gasPrice: tx.gasPrice,
        gasUsed: tx.gasUsed,
        fee: multiply(tx.gasPrice, tx.gasUsed),
        value: tx.value,
        input: tx.input,
        error: tx.isError === '1',
        asset,
        operations: [],
      };
      return parsedTx;
    },
  );

  let tokenTxns: IBlockScoutTokenTx[] = [];

  try {
    const tokenTxnsRes = await apiGetAccountTokenTx(address, chainId);
    if (isSuccessful(tokenTxnsRes)) {
      tokenTxns = tokenTxnsRes.data.result;
    }
  } catch (e) {
    // ignore
  }

  await Promise.all(
    tokenTxns.map(async (tokenTx: IBlockScoutTokenTx) => {
      const asset: IAssetData = {
        symbol: tokenTx.tokenSymbol,
        name: tokenTx.tokenName,
        decimals: tokenTx.tokenDecimal,
        contractAddress: tokenTx.contractAddress,
      };

      const functionHash = tokenTx.input.substring(0, 10);
      const functionMethod = await lookupMethod(functionHash);

      const functionName =
        functionMethod && functionMethod.name
          ? functionMethod.name
          : functionHash;

      const operation: ITxOperation = {
        asset,
        value: tokenTx.value,
        from: tokenTx.from,
        to: tokenTx.to,
        functionName,
      };

      let matchingTx = false;

      for (const tx of transactions) {
        if (tokenTx.hash.toLowerCase() === tx.hash.toLowerCase()) {
          tx.operations.push(operation);
          matchingTx = true;
          break;
        }
      }

      if (!matchingTx) {
        const asset: IAssetData = {
          symbol: 'ETH',
          name: 'Ethereum',
          decimals: '18',
          contractAddress: '',
        };

        const parsedTx: IParsedTx = {
          timestamp: multiply(tokenTx.timeStamp, 100),
          hash: tokenTx.hash,
          from: tokenTx.from,
          to: tokenTx.to,
          nonce: tokenTx.nonce,
          gasPrice: tokenTx.gasPrice,
          gasUsed: tokenTx.gasUsed,
          fee: multiply(tokenTx.gasPrice, tokenTx.gasUsed),
          value: tokenTx.value,
          input: tokenTx.input,
          error: false,
          asset,
          operations: [],
        };

        transactions.push(parsedTx);
      }
    }),
  );

  transactions.sort(
    (a, b) => parseInt(b.timestamp, 10) - parseInt(a.timestamp, 10),
  );

  return transactions;
}
