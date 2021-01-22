using System;
using Loex.SDK.Core.Client;
using Loex.SDK.Core.Log;
using Loex.SDK.Model.Response.Auth;
using Loex.SDK.Model.Response;

namespace Loex.SDK.Example
{
    public class MarketWebSocketClientExample
    {
        public static void RunAll()
        {
            //ReqAndSubscribeCandlestick();

           //ReqAndSubscribeDepth();

            //ReqAndSubscribeTrade();

            ReqAndSubscribeLast24Candlestick();
        }

        private static void ReqAndSubscribeCandlestick()
        {
            // Initialize a new instance
            var client = new CandlestickWebSocketClient(Config.Host);
            // Add the data receive handler
            client.OnDataReceived += Client_OnDataReceived;
            void Client_OnDataReceived(String response)
            {
                if (response != null)
                {
                    AppLogger.Info($"WebSocket returned data={response}");
                }
            }

            // Then connect to server and wait for the handler to handle the response
            client.Connect();

            // Request full data
            client.Req("btcusdt", "1day", 0, 0, "");

            client.Subscribe("btcusdt", "1day");

            Console.WriteLine("Press ENTER to unsubscribe and stop...\n");
            Console.ReadLine();

            // Unsubscrive the specific topic
            //client.UnSubscribe("btcusdt", "1min");

            //client.Subscribe("btcusdt", "1min", "j4ecd3s9rj.1610623898018.1.111");

            // Delete handler
            // Delete handler
            client.OnDataReceived -= Client_OnDataReceived;
        }

        private static void ReqAndSubscribeDepth()
        {
            var client = new DepthWebSocketClient(Config.Host);

            client.OnDataReceived += Client_OnDataReceived;
            void Client_OnDataReceived(String response)
            {
                if (response != null)
                {
                    AppLogger.Info($"WebSocket returned data={response}");
                }
            }

            // Then connect to server and wait for the handler to handle the response
            client.Connect();

            // Subscribe the specific topic
            client.Subscribe("btcusdt", "step0");

            Console.WriteLine("Press ENTER to unsubscribe and stop...\n");
            Console.ReadLine();

            // Unsubscrive the specific topic
            client.UnSubscribe("btcusdt", "step0");

            // Delete handler
            client.OnDataReceived -= Client_OnDataReceived;
        }


        private static void ReqAndSubscribeLast24Candlestick()
        {
            // Initialize a new instance
            var client = new Last24hCandlestickWebSocketClient(Config.Host);


            // Add the response receive handler
            void Client_OnDataReceived(String response)
            {
                if (response != null)
                {
                    AppLogger.Info($"WebSocket returned data={response}");
                }
            }

            // Then connect to server and wait for the handler to handle the response
            client.Connect();

            // Subscribe the specific topic
            client.Subscribe(null);

            Console.WriteLine("Press ENTER to unsubscribe and stop...\n");
            Console.ReadLine();

            // Unsubscrive the specific topic
            client.UnSubscribe(null);

            // Delete handler
            client.OnDataReceived -= Client_OnDataReceived;
        }

        private static void ReqAndSubscribeTrade()
        {
            // Initialize a new instance
            var client = new TradeWebSocketClient(Config.Host);
            // Add the data receive handler
            client.OnDataReceived += Client_OnDataReceived;
            void Client_OnDataReceived(String response)
            {
                if (response != null)
                {
                    AppLogger.Info($"WebSocket returned data={response}");
                }
            }

            // Then connect to server and wait for the handler to handle the response
            client.Connect();

            // Request full data
            client.Req("btcusdt", "");

            client.Subscribe("btcusdt", "");

            Console.WriteLine("Press ENTER to unsubscribe and stop...\n");
            Console.ReadLine();

            // Unsubscrive the specific topic
            client.UnSubscribe("btcusdt", "");

            // Delete handler
            // Delete handler
            client.OnDataReceived -= Client_OnDataReceived;
        }
    }
}
