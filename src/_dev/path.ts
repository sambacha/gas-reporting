// TODO
// Inital imports
const uniswapV2CloneGasSchedule = (fillData?: FillData) => {
    // TODO: Different base cost if to/from ETH.
    let gas = 90e3;
    const path = (fillData as UniswapV2FillData).tokenAddressPath;
    if (path.length > 2) {
        gas += (path.length - 2) * 60e3; // +60k for each hop.
    }
    return gas;
};
/**
 * Calculated gross gas cost of the underlying exchange.
 * The cost of switching from one source to another, assuming
 * we are in the middle of a transaction.
 * I.e remove the overhead cost of ExchangeProxy (130k) and
 * the ethereum transaction cost (21k)
 */
// tslint:disable:custom-no-magic-numbers
export const DEFAULT_GAS_SCHEDULE: Required<FeeSchedule> = {
    [ERC20BridgeSource.Native]: fillData => {
        // TODO jacob re-order imports so there is no circular rependency with SignedNativeOrder
        const nativeFillData = fillData as { type: FillQuoteTransformerOrderType };
        return nativeFillData && nativeFillData.type === FillQuoteTransformerOrderType.Limit
            ? PROTOCOL_FEE_MULTIPLIER.plus(100e3).toNumber()
            : // TODO jacob revisit wth v4 LimitOrders
              100e3;
    },
    [ERC20BridgeSource.Uniswap]: () => 90e3,
    [ERC20BridgeSource.LiquidityProvider]: fillData => {
        return (fillData as LiquidityProviderFillData).gasCost || 100e3;
    },
    [ERC20BridgeSource.Eth2Dai]: () => 400e3,
    [ERC20BridgeSource.Kyber]: () => 450e3,
    [ERC20BridgeSource.Curve]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.CurveV2]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.Swerve]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.SnowSwap]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.Nerve]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.Belt]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.Ellipsis]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.Smoothy]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.Saddle]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.IronSwap]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.XSigma]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.FirebirdOneSwap]: fillData => (fillData as CurveFillData).pool.gasSchedule,
    [ERC20BridgeSource.MultiBridge]: () => 350e3,
    [ERC20BridgeSource.UniswapV2]: uniswapV2CloneGasSchedule,
    [ERC20BridgeSource.SushiSwap]: uniswapV2CloneGasSchedule,
    [ERC20BridgeSource.CryptoCom]: uniswapV2CloneGasSchedule,
    [ERC20BridgeSource.Linkswap]: uniswapV2CloneGasSchedule,
    [ERC20BridgeSource.ShibaSwap]: uniswapV2CloneGasSchedule,
    [ERC20BridgeSource.Balancer]: () => 120e3,
    [ERC20BridgeSource.BalancerV2]: () => 100e3,
    [ERC20BridgeSource.Cream]: () => 120e3,
    [ERC20BridgeSource.MStable]: () => 200e3,
    [ERC20BridgeSource.MakerPsm]: (fillData?: FillData) => {
        const psmFillData = fillData as MakerPsmFillData;
        return psmFillData.takerToken === psmFillData.gemTokenAddress ? 210e3 : 290e3;
    },
    [ERC20BridgeSource.Mooniswap]: () => 130e3,
    [ERC20BridgeSource.Shell]: () => 170e3,
    [ERC20BridgeSource.Component]: () => 188e3,
    [ERC20BridgeSource.MultiHop]: (fillData?: FillData) => {
        const firstHop = (fillData as MultiHopFillData).firstHopSource;
        const secondHop = (fillData as MultiHopFillData).secondHopSource;
        const firstHopGas = DEFAULT_GAS_SCHEDULE[firstHop.source](firstHop.fillData);
        const secondHopGas = DEFAULT_GAS_SCHEDULE[secondHop.source](secondHop.fillData);
        return new BigNumber(firstHopGas)
            .plus(secondHopGas)
            .plus(30e3)
            .toNumber();
    },
    [ERC20BridgeSource.Dodo]: (fillData?: FillData) => {
        const isSellBase = (fillData as DODOFillData).isSellBase;
        // Sell base is cheaper as it is natively supported
        // sell quote requires additional calculation and overhead
        return isSellBase ? 180e3 : 300e3;
    },
    [ERC20BridgeSource.DodoV2]: (_fillData?: FillData) => 100e3,
    [ERC20BridgeSource.Bancor]: (fillData?: FillData) => {
        let gas = 200e3;
        const path = (fillData as BancorFillData).path;
        if (path.length > 2) {
            gas += (path.length - 2) * 60e3; // +60k for each hop.
        }
        return gas;
    },
    [ERC20BridgeSource.KyberDmm]: (fillData?: FillData) => {
        // TODO: Different base cost if to/from ETH.
        let gas = 95e3;
        const path = (fillData as UniswapV2FillData).tokenAddressPath;
        if (path.length > 2) {
            gas += (path.length - 2) * 65e3; // +65k for each hop.
        }
        return gas;
    },
    [ERC20BridgeSource.UniswapV3]: (fillData?: FillData) => {
        let gas = 100e3;
        const path = (fillData as UniswapV3FillData).tokenAddressPath;
        if (path.length > 2) {
            gas += (path.length - 2) * 32e3; // +32k for each hop.
        }
        return gas;
    },
