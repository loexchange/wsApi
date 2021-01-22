using System;
using System.Security.Cryptography;
using System.Text;

namespace Loex.SDK.Core.RequestBuilder
{
    /// <summary>
    /// Responsible to generate signature
    /// </summary>
    public class Signer : IDisposable
    {
        HMACSHA256 _hmacsha256;

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="key">The secrect key that is used to sign</param>
        public Signer(string key)
        {
            byte[] keyBuffer = Encoding.UTF8.GetBytes(key);
            _hmacsha256 = new HMACSHA256(keyBuffer);
        }

        public string Sign(string input)
        {
            if (string.IsNullOrEmpty(input))
            {
                return string.Empty;
            }

            byte[] inputBuffer = Encoding.UTF8.GetBytes(input);

            byte[] hashedBuffer = _hmacsha256.ComputeHash(inputBuffer);

            return Convert.ToBase64String(hashedBuffer);
        }

        #region IDisposable Support
        private bool isDisposed = false;

        protected virtual void Dispose(bool disposing)
        {
            if (!isDisposed)
            {
                if (disposing)
                {
                    _hmacsha256.Dispose();
                }

                isDisposed = true;
            }
        }

        public void Dispose()
        {
            Dispose(true);
        }
        #endregion


    }
}
