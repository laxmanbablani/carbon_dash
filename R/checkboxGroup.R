# AUTO GENERATED FILE - DO NOT EDIT

#' @export
checkboxGroup <- function(children=NULL, id=NULL, className=NULL, decorator=NULL, helperText=NULL, invalid=NULL, invalidText=NULL, legendId=NULL, legendText=NULL, loading_state=NULL, orientation=NULL, readOnly=NULL, slug=NULL, style=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, decorator=decorator, helperText=helperText, invalid=invalid, invalidText=invalidText, legendId=legendId, legendText=legendText, loading_state=loading_state, orientation=orientation, readOnly=readOnly, slug=slug, style=style, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CheckboxGroup',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'decorator', 'helperText', 'invalid', 'invalidText', 'legendId', 'legendText', 'loading_state', 'orientation', 'readOnly', 'slug', 'style', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
