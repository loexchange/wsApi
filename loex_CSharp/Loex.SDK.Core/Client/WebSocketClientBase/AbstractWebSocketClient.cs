﻿using System;
using Loex.SDK.Core.Log;

namespace Loex.SDK.Core.Client.WebSocketClientBase
{
    public abstract class AbstractWebSocketClient
    {
        protected ILogger _logger = new ConsoleLogger();

        public void SetLogger(ILogger logger)
        {
            _logger = logger ?? new EmptyLogger();
        }

        public abstract void Connect(bool autoConnect = true);

        public abstract void Disconnect();
    }
}
