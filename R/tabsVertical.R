# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tabsVertical <- function(children=NULL, id=NULL, className=NULL, defaultSelectedIndex=NULL, height=NULL, loading_state=NULL, onChange=NULL, selectedIndex=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultSelectedIndex=defaultSelectedIndex, height=height, loading_state=loading_state, onChange=onChange, selectedIndex=selectedIndex, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TabsVertical',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultSelectedIndex', 'height', 'loading_state', 'onChange', 'selectedIndex', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
