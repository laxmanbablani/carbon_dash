# AUTO GENERATED FILE - DO NOT EDIT

#' @export
loading <- function(children=NULL, id=NULL, active=NULL, className=NULL, description=NULL, loading_state=NULL, small=NULL, style=NULL, withOverlay=NULL) {
    
    props <- list(children=children, id=id, active=active, className=className, description=description, loading_state=loading_state, small=small, style=style, withOverlay=withOverlay)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Loading',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'active', 'className', 'description', 'loading_state', 'small', 'style', 'withOverlay'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
