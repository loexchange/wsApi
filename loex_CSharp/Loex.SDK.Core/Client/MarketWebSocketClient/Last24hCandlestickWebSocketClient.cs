using Loex.SDK.Core.Client.WebSocketClientBase;
using Loex.SDK.Core.Log;

namespace Loex.SDK.Core.Client
{
    /// <summary>
    /// Responsible to handle last 24h candlestick data from WebSocket
    /// </summary>
    public class Last24hCandlestickWebSocketClient : WebSocketV2ClientBase
    {

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="host">websockethost</param>
        public Last24hCandlestickWebSocketClient(string host = DEFAULT_HOST)
             : base("", "", host)
        {
        }

        /// <summary>
        /// Subscribe latest 24h market stats
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="clientId">Client id</param>
        public void Subscribe(string symbol, string clientId = "")
        {
            string topic = "";
            if (symbol == null)
            {
                topic = "market_ticker";
            }
            else
            {
                topic = $"market_{symbol}_ticker";
            }
            _WebSocket.Send($"{{\"action\": \"sub\",\"ch\": \"{topic}\"}}");

            _logger.Log(LogLevel.Info, $"WebSocket subscribed, topic={topic}, clientId={clientId}");
        }

        /// <summary>
        /// Unsubscribe latest 24 market stats
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="clientId">Client id</param>
        public void UnSubscribe(string symbol, string clientId = "")
        {
            string topic = "";
            if (symbol == null)
            {
                topic = $"market_ticker";
            }
            else
            {
                topic = $"market_{symbol}_ticker";
            }

            _WebSocket.Send($"{{\"action\": \"unsub\",\"ch\": \"{topic}\" }}");

            _logger.Log(LogLevel.Info, $"WebSocket unsubscribed, topic={topic}, clientId={clientId}");
        }
    }
}
