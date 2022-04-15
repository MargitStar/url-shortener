import { useState } from 'react';
import axios from 'axios';

const baseAPIUrl = "http://127.0.0.1:5000/";

const App = () => {
  const [url, setURL] = useState('')
  const [shortURL, setShortURL] = useState()

  const shortURLLink = `${baseAPIUrl}${shortURL}/`

  const isValidURL = url =>{
    return url.startsWith("http:") || url.startsWith("https:");
  }

  const changeHandler = (e) => {
    setURL(e.target.value)
  }

  const clickHandler = async () => {
    if (isValidURL(url)) {
      const response = await axios.post(`${baseAPIUrl}api/long-urls/`, {"long_url": url });
      setShortURL(response.data.short_url)
    }
  }

  return (
    <div>
      <header>
        <h1>URL SHORTENER</h1>
        <input type="text" name="input" placeholder="Type here" onChange={changeHandler} value={url} />
        <button type="button" onClick={clickHandler}>Generate short URL</button>
        <div>
          { shortURL && (<a href={shortURLLink} target="_blank">{shortURLLink}</a>) }
        </div>
      </header>
    </div>
  );
}

export default App;
