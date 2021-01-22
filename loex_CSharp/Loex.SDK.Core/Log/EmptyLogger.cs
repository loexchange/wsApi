using System;
namespace Loex.SDK.Core.Log
{
    public class EmptyLogger : ILogger
    {
        public void Log(LogLevel level, string message)
        {
            return;
        }
    }
}
