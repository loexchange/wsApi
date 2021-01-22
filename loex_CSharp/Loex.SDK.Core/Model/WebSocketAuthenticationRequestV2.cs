using System;
using Newtonsoft.Json;

namespace Loex.SDK.Core.Model
{
    public class WebSocketAuthenticationRequestV2
    {
        public class Params
        {
            public string apiKey;
            public string signatureMethod { get { return "HmacSHA256"; } }
            public string signatureVersion { get { return "1.0"; } }
            public string timestamp;
            public string signature;
        }

        public string action { get { return "req"; } }
        public string ch { get { return "auth"; } }
        public Params @params;

        public string ToJson()
        {
            return JsonConvert.SerializeObject(this);
        }
    }

}
