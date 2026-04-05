# AUTO GENERATED FILE - DO NOT EDIT

#' @export
headerGlobalAction <- function(children=NULL, id=NULL, className=NULL, isActive=NULL, loading_state=NULL, onClick=NULL, style=NULL, tooltipAlignment=NULL, tooltipDropShadow=NULL, tooltipHighContrast=NULL) {
    
    props <- list(children=children, id=id, className=className, isActive=isActive, loading_state=loading_state, onClick=onClick, style=style, tooltipAlignment=tooltipAlignment, tooltipDropShadow=tooltipDropShadow, tooltipHighContrast=tooltipHighContrast)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'HeaderGlobalAction',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'isActive', 'loading_state', 'onClick', 'style', 'tooltipAlignment', 'tooltipDropShadow', 'tooltipHighContrast'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
