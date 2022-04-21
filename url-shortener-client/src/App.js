import { useState } from 'react';
import './App.css';
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
    <div className='main-container'>
      <div className='form-container'>
          <h1 className='title'>URL Shortener</h1>
          <h3 className='description'>ShortURL allows to reduce long links from Instagram, Facebook, YouTube, Twitter,
            Linked In and top sites on the Internet, just paste the long URL and click the Shorten URL button.</h3>
          <div className='form'>
            <div className='input-container'>
              <input type="text" name="input" placeholder="Type here" onChange={changeHandler} value={url} className='input'/>
              <button type="button" onClick={clickHandler} className='short-url-button'>Short URL</button>
            </div>
          </div>
              { shortURL && (<div className='shorten-link-form'><h3>Short URL <a className='shorten-link' href={shortURLLink} target="_blank">{shortURLLink}</a></h3></div>) }
          </div>
    </div>
  );
}

export default App;
