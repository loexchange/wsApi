using Loex.SDK.Core.Client.WebSocketClientBase;
using Loex.SDK.Core.Log;

namespace Loex.SDK.Core.Client
{
    /// <summary>
    /// Responsible to handle Depth data from WebSocket
    /// </summary>
    public class DepthWebSocketClient : WebSocketV2ClientBase
    {

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="host">websockethost</param>
        public DepthWebSocketClient(string host = DEFAULT_HOST)
            :base("", "", host)
        {
        }


        /// <summary>
        /// Subscribe latest market by price order book in snapshot mode at 1-second interval.
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="type">Market depth aggregation level</param>
        /// <param name="clientId">Client id</param>
        public void Subscribe(string symbol, string type, string clientId = "")
        {
            string topic = $"market_{symbol}_depth_{type}";

            _WebSocket.Send($"{{\"action\": \"sub\",\"ch\": \"{topic}\"}}");

            _logger.Log(LogLevel.Info, $"WebSocket subscribed, topic={topic}, clientId={clientId}");
        }

        /// <summary>
        /// Unsubscribe market by price order book
        /// </summary>
        /// <param name="symbol">Trading symbol</param>
        /// <param name="type">Market depth aggregation level</param>
        /// <param name="clientId">Client id</param>
        public void UnSubscribe(string symbol, string type, string clientId = "")
        {
            string topic = $"market_{symbol}_depth_{type}";

            _WebSocket.Send($"{{\"action\": \"unsub\",\"ch\": \"{topic}\"}}");

            _logger.Log(LogLevel.Info, $"WebSocket subscribed, topic={topic}, clientId={clientId}");
        }
    }
}
