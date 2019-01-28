export function fetchArticles() {
  return dispatch => {
    let headers = {"Content-Type": "application/json"};
    return fetch("http://127.0.0.1:8000/api/articles/", {headers, })
      .then(res => res.json())
      .then(articles => {
        return dispatch({
          type: 'FETCH_ARTICLES',
          articles
        })
      })
  }
}


export function addArticle(article_name,created_by,created_at,topic) {
  return dispatch => {
    let headers = {"Content-Type": "application/json"};
    let body = JSON.stringify({article_name, created_by,created_at,topic});
    return fetch("http://127.0.0.1:8000/api/articles/", {headers, method: "POST", body})
      .then(res => res.json())
      .then(article => {
        return dispatch({
          type: 'ADD_ARTICLE',
          article
        })
      })
  }
}


export function updateArticle(index, article_name){
  return (dispatch, getState) => {

    let headers = {"Content-Type": "application/json"};
    let body = JSON.stringify({article_name, });
    let articleId = getState().articles[index].id;
    let base_url = "http://127.0.0.1:8000/api/articles/"+articleId+"/";

    return fetch(base_url, {headers, method: "PUT", body})
      .then(res => res.json())
      .then(article => {
        return dispatch({
          type: 'UPDATE_ARTICLE',
          article,
          index
        })
      })
  }
}

export function deleteArticle(id) {
  return {
    type: 'DELETE_ARTICLE',
    id
  }
}