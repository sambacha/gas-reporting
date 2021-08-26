const gas = require("./src/gas.json");
const mainnet = require("/src/chains/mainnet.json");
const goerli = require("/src/chains/goerli.json");
const matic = require("/src/chains/matic.json");
const maticTestnet = require("/src/chains/matic-testnet.json");
const xdai = require("/src/chains/xdai.json");
const bsc = require("/src/chains/bsc.json");
const bscTestnet = require("/src/chains/bsc-testnet.json");
const heco = require("/src/chains/heco.json");
const hecoTestnet = require("/src/chains/heco-testnet.json");
const okex = require("/src/chains/okex.json");
const okexTestnet = require("/src/chains/okex-testnet.json");


module.exports = function buildList() {
  const parsed = version.split(".");
  return {
    name: "Multi-Chain Transaction Pricing",
    timestamp: new Date().toISOString(),
    version: {
      major: +parsed[0],
      minor: +parsed[1],
      patch: +parsed[2],
    },
    tags: {},
    keywords: ["gas", "transaction price", "gwei"],
    gas: [
        ...mainnet,
        ...goerli,
        ...matic,
        ...maticTestnet,
        ...xdai,
        ...bsc,
        ...bscTestnet,
        ...heco,
        ...hecoTestnet,
        ...okex,
        ...okexTestnet,
    ]
    // sort them by symbol for easy readability
    .sort((t1, t2) => {
      if (t1.chainId === t2.chainId) {
        return t1.symbol.toLowerCase() < t2.symbol.toLowerCase() ? -1 : 1;
      }
      return t1.chainId < t2.chainId ? -1 : 1;
    }),
};
};