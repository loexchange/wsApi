using System;
using Loex.SDK.Core.Client;
using Loex.SDK.Model.Response;
using Loex.SDK.Model.Response.Account;
using Loex.SDK.Model.Response.Auth;

namespace Loex.SDK.Example
{
    public class AccountWebSocketClientExample
    {
        public static void RunAll()
        {
            SubscribeAccount();
        }

        

        private static void SubscribeAccount()
        {
            // Initialize a new instance
            var client = new SubscribeAccountWebSocketClient(Config.AccessKey, Config.SecretKey, Config.Host);

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

            client.Subscribe("111111111");


            Console.WriteLine("Press ENTER to unsubscribe and stop...\n");
            Console.ReadLine();

            // Unsubscrive the specific topic
            //client.UnSubscribe("1");

            // Delete handler
            client.OnDataReceived -= Client_OnDataReceived;
        }
    }
}
