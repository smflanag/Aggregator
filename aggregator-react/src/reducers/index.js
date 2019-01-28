import { combineReducers } from 'redux';
import articles from "./articles";


const aggregatorApp = combineReducers({
  articles,
})

export default aggregatorApp;