import { useState } from "react";
import CryptoJS from "crypto-js";

function generateRandomKeyAndIV() {
  const key = CryptoJS.lib.WordArray.random(32);
  const iv = CryptoJS.lib.WordArray.random(16);
  return { key, iv };
}

function encryptWithAES(text, key, iv) {
  const encrypted = CryptoJS.AES.encrypt(text, key, { iv }).toString();
  return encrypted;
}

function decryptWithAES(encryptedData, key, iv) {
  const decrypted = CryptoJS.AES.decrypt(encryptedData, key, { iv }).toString(
    CryptoJS.enc.Utf8
  );
  return decrypted;
}

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [encryptedData, setEncryptedData] = useState("");
  const [decryptedData, setDecryptedData] = useState("");
  const { key, iv } = generateRandomKeyAndIV();

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(email);
    console.log(password);
    const encrypted = encryptWithAES(password, key, iv);
    setEncryptedData(encrypted);
    const decrypted = decryptWithAES(encrypted, key, iv);
    setDecryptedData(decrypted);
    setEmail("");
    setPassword("");
  };

  return (
    <>
      <div className="container">
        <form className="my-3" onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">
              Email address
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
              }}
              className="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
            />
          </div>
          <div className="mb-3">
            <label htmlFor="exampleInputPassword1" className="form-label">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
              }}
              autoComplete="false"
              className="form-control"
              id="exampleInputPassword1"
            />
          </div>

          <button type="submit" className="btn btn-primary">
            Submit
          </button>

          <div className="my-3">
            <label htmlFor="encrypted" className="form-label">
              Encrypted data for Password
            </label>
            <div className="form-control p-3">{encryptedData}</div>
          </div>
          <div className="my-3">
            <label htmlFor="encrypted" className="form-label">
              Decrypted data for Password
            </label>
            <div className="form-control p-3">{decryptedData}</div>
          </div>
        </form>
      </div>
    </>
  );
}

export default App;
