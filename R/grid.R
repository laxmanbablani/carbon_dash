# AUTO GENERATED FILE - DO NOT EDIT

#' @export
grid <- function(children=NULL, id=NULL, align=NULL, as_=NULL, className=NULL, condensed=NULL, fullWidth=NULL, loading_state=NULL, narrow=NULL, style=NULL) {
    
    props <- list(children=children, id=id, align=align, as_=as_, className=className, condensed=condensed, fullWidth=fullWidth, loading_state=loading_state, narrow=narrow, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Grid',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'as_', 'className', 'condensed', 'fullWidth', 'loading_state', 'narrow', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
