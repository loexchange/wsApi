using Loex.SDK.Core.Client.WebSocketClientBase;
using Xunit;

namespace Loex.SDK.Core.Test
{
    public class GZipDecompresserTest
    {
        [Fact]
        public void Decompress_Success()
        {
            byte[] compressed = GZipDecompresser.Compress("Loex");

            string origin = GZipDecompresser.Decompress(compressed);

            Assert.Equal("Loex", origin);
        }
    }
}
