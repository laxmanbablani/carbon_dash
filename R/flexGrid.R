# AUTO GENERATED FILE - DO NOT EDIT

#' @export
flexGrid <- function(children=NULL, id=NULL, as_=NULL, className=NULL, condensed=NULL, fullWidth=NULL, loading_state=NULL, narrow=NULL, style=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, condensed=condensed, fullWidth=fullWidth, loading_state=loading_state, narrow=narrow, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FlexGrid',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'condensed', 'fullWidth', 'loading_state', 'narrow', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
