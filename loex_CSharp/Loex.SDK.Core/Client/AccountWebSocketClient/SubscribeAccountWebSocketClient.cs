using Loex.SDK.Core.Client.WebSocketClientBase;
using Loex.SDK.Core.Log;
using Loex.SDK.Model.Response.Account;

namespace Loex.SDK.Core.Client
{
    /// <summary>
    /// Responsible to handle account asset subscription from WebSocket
    /// This need authentication version 2
    /// </summary>
    public class SubscribeAccountWebSocketClient : WebSocketV2ClientBase
    {
        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="accessKey">API Access Key</param>
        /// <param name="secretKey">API Secret Key</param>
        /// <param name="host">API Host</param>
        public SubscribeAccountWebSocketClient(string accessKey, string secretKey, string host = DEFAULT_HOST)
            :base(accessKey, secretKey, host)
        {
        }

        /// <summary>
        /// Subscribe all balance updates of the current account
        /// </summary>
        /// 0: Only update when account balance changed
        /// 1: Update when either account balance changed or available balance changed</param>
        /// <param name="clientId">Client id</param>
        public void Subscribe(string clientId = "")
        {
            string topic = $"accounts_update";

            _WebSocket.Send($"{{\"action\":\"sub\", \"cid\": \"{clientId}\", \"ch\":\"{topic}\"}}");

            _logger.Log(LogLevel.Info, $"WebSocket subscribed, topic={topic}");
        }

        /// <summary>
        /// Unsubscribe balance updates
        /// </summary>
        /// <param name="clientId">Client id</param>
        public void UnSubscribe(string mode, string clientId = "")
        {
            string topic = $"accounts_update";

            _WebSocket.Send($"{{\"action\":\"unsub\", \"cid\": \"{clientId}\", \"ch\":\"{topic}\" }}");

            _logger.Log(LogLevel.Info, $"WebSocket unsubscribed, topic={topic}");
        }
    }
}
