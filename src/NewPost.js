import React, {Component} from "react";
import { Redirect} from "react-router-dom";
import axios from 'axios';


class NewPost extends Component {

  state = {};

    create_post = (article_title, article_content, topic, user) => {
        var today = new Date();
        var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        var timestamp = date+' '+time;
        axios.post('/api/article_view', {
            created_by: user,
            created_at: timestamp,
            article_name: article_title,
            article_content: article_content,
            topic: topic
            })
          .then(res => {
            if (res.status === 200) {
              this.props.history.push('/articles');
            } else if (res.status === 401 || res.status === 403) {
              console.log("AUTHENTICATION_ERROR");
              throw res.data;
            }
      })
    }
    onSubmit = e => {
    e.preventDefault();
    this.create_post(this.state.article_title, this.state.article_content, window.current_topic, window.user);
  }

  render() {
    if (!window.token === "") {
      return <Redirect to="/" />
    }
    return (
    <div>
        <div>
            <form onSubmit={this.onSubmit}>
                <fieldset>
                  <legend>New Post</legend>
                  <p>
                    <label htmlFor="article_title">Article Title </label>
                    <input
                      type="text" id="article_title"
                      onChange={e => this.setState({article_title: e.target.value})} />
                  </p>
                  <p>
                    <label htmlFor="article_content">Article Content </label>
                    <input
                      type="text" id="article_content"
                      onChange={e => this.setState({article_content: e.target.value})} />
                  </p>
                  <p>
                    <button type="submit">Add Post</button>
                  </p>


                </fieldset>
            </form>
        </div>

    </div>
    )
  }
}


export default NewPost;