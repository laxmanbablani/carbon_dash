# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tag <- function(children=NULL, id=NULL, as_=NULL, className=NULL, decorator=NULL, disabled=NULL, filter=NULL, loading_state=NULL, onClose=NULL, renderIcon=NULL, size=NULL, slug=NULL, style=NULL, title=NULL, type=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, decorator=decorator, disabled=disabled, filter=filter, loading_state=loading_state, onClose=onClose, renderIcon=renderIcon, size=size, slug=slug, style=style, title=title, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Tag',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'decorator', 'disabled', 'filter', 'loading_state', 'onClose', 'renderIcon', 'size', 'slug', 'style', 'title', 'type'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
