using Loex.SDK.Core.Log;

namespace Loex.SDK.Example
{
    class Program
    {
        static void Main(string[] args)
        {
            AppLogger.Info("Example started");

            Config.LoadConfig();

            //AccountWebSocketClientExample.RunAll();

            //MarketWebSocketClientExample.RunAll();

            OrderWebSocketClientExample.RunAll();

            AppLogger.Info("Example stopped");
        }


    }
}
