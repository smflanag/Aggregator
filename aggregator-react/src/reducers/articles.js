const initialState = [];


export default function articles(state=initialState, action) {
    let articleList = state.slice();

  switch (action.type) {

    case 'FETCH_ARTICLES':
    return [...state, ...action.articles];

    case 'ADD_ARTICLE':
      return [...state, action.article];

    case 'UPDATE_ARTICLE':
      let articleToUpdate = articleList[action.index]
      articleToUpdate.article_name = action.article.article_name;
      articleList.splice(action.index, 1, articleToUpdate);
      return articleList;

    case 'DELETE_ARTICLE':
      articleList.splice(action.id, 1);
      return articleList;

    default:
      return state;
  }
}