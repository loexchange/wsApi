using System;
using Loex.SDK.Core.Client;
using Loex.SDK.Model.Response;
using Loex.SDK.Model.Response.Auth;

namespace Loex.SDK.Example
{
    public class TraderExample
    {
        public static void Run()
        {
            string symbol = "hthusd";

            var client = SubscribeOrderV2(symbol);

            Console.WriteLine("Press ENTER to place an order...\n");
            Console.ReadLine();


            Console.WriteLine("Press ENTER to unsubscribe and exit...\n");
            Console.ReadLine();

            UnsubscribeOrderV2(client, symbol);
        }


        private static SubscribeOrderWebSocketV2Client SubscribeOrderV2(string symbol)
        {
            // Initialize a new instance
            var client = new SubscribeOrderWebSocketV2Client(Config.AccessKey, Config.SecretKey);

            // Add the auth receive handler
            client.OnAuthenticationReceived += Client_OnAuthReceived;
            void Client_OnAuthReceived(WebSocketV2AuthResponse response)
            {
                if (response.code == (int)ResponseCode.Success)
                {
                    // Subscribe the specific topic
                    //client.Subscribe("1");
                    AppLogger.Info($"WebSocket authentication success, code={response.code}");
                }
                else
                {
                    AppLogger.Error($"WebSocket authentication fail, code={response.code}, message={response.message}");
                }
            }

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

            return client;
        }

        private static void UnsubscribeOrderV2(SubscribeOrderWebSocketV2Client client, string symbol)
        {
            // Unsubscrive the specific topic
            client.UnSubscribe(symbol);
        }
    }
}
