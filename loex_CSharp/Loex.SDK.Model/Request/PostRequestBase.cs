using Newtonsoft.Json;

namespace Loex.SDK.Model.Request
{
    public class PostRequestBase
    {
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this);
        }
    }
}
