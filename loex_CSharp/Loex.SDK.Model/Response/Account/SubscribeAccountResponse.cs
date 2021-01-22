using Loex.SDK.Model.Response.WebSocket;

namespace Loex.SDK.Model.Response.Account
{
    /// <summary>
    /// SubscribeAccountV2 response
    /// </summary>
    public class SubscribeAccountResponse : WebSocketV2ResponseBase
    {
        /// <summary>
        /// Response body from sub
        /// </summary>
        public AccountUpdate data;

        public class AccountUpdate
        {
            /// <summary>
            /// The crypto currency of this balance
            /// </summary>
            public string coin;

            /// <summary>
            /// The account id of this individual balance
            /// </summary>
            public int account;

            /// <summary>
            /// The account balance (only exists when account balance changed)
            /// </summary>
            public string balance;

            /// <summary>
            /// Change type
            /// Possible values: [order-place,order-match,order-refund,order-cancel,order-fee-refund,
            /// margin-transfer,margin-loan,margin-interest,margin-repay,deposit, withdraw, other]
            /// </summary>
            public string changeType;

            /// <summary>
            /// Account type
            /// Possible values: [trade, frozen, loan, interest]
            /// </summary>
            public string accountType;

            /// <summary>
            /// Change timestamp in millisecond
            /// If it is null, then this message is account overview not update
            /// </summary>
            public long? changeTime;
        }
    }
}
