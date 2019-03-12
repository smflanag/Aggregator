import React from 'react'
import ReactDOM from 'react-dom'

class Test extends React.Component {
    render() {
        var list = window.props;
        return <div>{list.map(item => <TestChild key={item.pk}
                        article={item.article_name}/> )}</div>;
    }
}

class TestChild extends React.Component {
    render() {
     return <li><b>{this.props.article}</b></li>;
    }
}


ReactDOM.render(
    <Test/>,
    document.getElementById('react'),
);