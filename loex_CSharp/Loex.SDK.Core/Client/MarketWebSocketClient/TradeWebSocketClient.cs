using Loex.SDK.Core.Client.WebSocketClientBase;
using Loex.SDK.Core.Log;

namespace Loex.SDK.Core.Client
{
    /// <summary>
    /// Responsible to handle Trade data from WebSocket
    /// </summary>
    public class TradeWebSocketClient : WebSocketV2ClientBase
    { 

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="host">websockethost</param>
    public TradeWebSocketClient(string host = DEFAULT_HOST)
            :base("", "", host)
        {
        }

        /// <summary>
        /// Request latest 300 trade data
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="clientId">Client id</param>
        public void Req(string symbol, string clientId = "")
        {
            string topic = $"market_{symbol}_trade_ticker";

            _WebSocket.Send($"{{\"action\": \"req\",\"ch\": \"{topic}\" }}");

            _logger.Log(LogLevel.Info, $"WebSocket requested, topic={topic}, clientId={clientId}");
        }


        /// <summary>
        /// Subscribe latest completed trade in tick by tick mode
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="clientId">Client id</param>
        public void Subscribe(string symbol, string clientId = "")
        {
            string topic = $"market_{symbol}_trade_ticker";

            _WebSocket.Send($"{{\"action\": \"sub\", \"ch\": \"{topic}\" }}");

            _logger.Log(LogLevel.Info, $"WebSocket subscribed, topic={topic}, clientId={clientId}");
        }

        /// <summary>
        /// Unsubscribe trade
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="clientId">Client id</param>
        public void UnSubscribe(string symbol, string clientId = "")
        {
            string topic = $"market_{symbol}_trade_ticker";

            _WebSocket.Send($"{{\"action\": \"unsub\", \"ch\": \"{topic}\"}}");

            _logger.Log(LogLevel.Info, $"WebSocket unsubscribed, topic={topic}, clientId={clientId}");
        }
    }
}
