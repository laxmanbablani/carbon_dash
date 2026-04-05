# AUTO GENERATED FILE - DO NOT EDIT

#' @export
link <- function(children=NULL, id=NULL, as_=NULL, className=NULL, disabled=NULL, href=NULL, inline=NULL, loading_state=NULL, renderIcon=NULL, size=NULL, style=NULL, visited=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, disabled=disabled, href=href, inline=inline, loading_state=loading_state, renderIcon=renderIcon, size=size, style=style, visited=visited)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Link',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'disabled', 'href', 'inline', 'loading_state', 'renderIcon', 'size', 'style', 'visited'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
