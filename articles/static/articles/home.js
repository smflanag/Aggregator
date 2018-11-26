<script id="article_template" type="x-tmpl-mustache">

   <div class="container article_lists">
            <div class="row">
                {{#articles}}
                <div class="col-md-5">
                    <h2><a>{{article}}</a></h2>
                </div>
                <div class="col-md-2 text-truncate">
                    <h6>Topic: <a>{{topic}}</a></h6>
                </div>
                <div class="col-md-2">
                    <h6>Created by: <a>{{user}}</a></h6>
                </div>
                <div class="col-md-3">
                    <h6>Created at:{{time}}</h6>
                {{/articles}}
                </div>
            </div>
        </div>
</script>