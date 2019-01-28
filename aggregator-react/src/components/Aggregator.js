import React, { Component } from 'react';
import {connect} from 'react-redux';
import {articles} from "../actions";

class Aggregator extends Component {

    componentDidMount() {
    this.props.fetchArticles();
}

    state = {
  article_name: "",
  updateArticleId: null}

    resetForm = () => {
        this.setState({
  article_name: "",
  updateArticleId: null});
    }

    selectForEdit = (id) => {
        let article = this.props.articles[id];
        this.setState({
  article_name: article.article_name,
  updateArticleId: id});
    }


  submitArticle = (e) => {
  e.preventDefault();
  if (this.state.updateArticleId === null) {
    this.props.addArticle(this.state.article_name, this.state.created_at, this.state.created_by, this.state.topic).then(this.resetForm());
  } else {
    this.props.updateArticle(this.state.updateArticleId,this.state.article_name).then(this.resetForm);
  }
}

  render() {
    return (
      <div>
        <h2>Welcome to Aggregator!</h2>
        <hr />

        <h3>Add article</h3>
            <form onSubmit={this.submitArticle}>
              <input
                value={this.state.article_name}
                placeholder="Enter article name here..."
                onChange={(e) => this.setState({article_name: e.target.value})}
                required />
                <input
                value={this.state.created_by}
                placeholder="Enter author here..."
                onChange={(e) => this.setState({created_by: e.target.value})}
                required />
                <input
                value={this.state.created_at}
                placeholder="Enter time here..."
                onChange={(e) => this.setState({created_at: e.target.value})}
                required />
                <input
                value={this.state.topic}
                placeholder="Enter topic here..."
                onChange={(e) => this.setState({topic: e.target.value})}
                required />
                <button onClick={this.resetForm}>Reset</button>
              <input type="submit" value="Save Article" />
            </form>

        <h3>Articles</h3>
        <table>
          <tbody>
            {this.props.articles.map((article, id) => (
              <tr key={`article_${article.id}`}>
                <td>{article.article_name}</td>
                <td>{article.topic}</td>
                <td>{article.created_by}</td>
                <td>{article.created_at}</td>
                <td><button onClick={() => this.selectForEdit(id)}>edit</button></td>
                <td><button onClick={() => this.props.deleteArticle(id)}>delete</button></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    )
  }
}


const mapStateToProps = state => {
  return {
    articles: state.articles,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    fetchArticles: () => {
      dispatch(articles.fetchArticles());
    },

    addArticle: (created_by,created_at,article_name,topic) => {
        return dispatch(articles.addArticle(created_by,created_at,article_name,topic));
    },
    updateArticle: (id, created_by,created_at,article_name,topic) => {
      return dispatch(articles.updateArticle(id,created_by,created_at,article_name,topic));
    },
    deleteArticle: (id) => {
      dispatch(articles.deleteArticles(id));
    },
  }
}


export default connect(mapStateToProps, mapDispatchToProps)(Aggregator);