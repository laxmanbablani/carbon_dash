# AUTO GENERATED FILE - DO NOT EDIT

#' @export
copy <- function(children=NULL, id=NULL, align=NULL, autoAlign=NULL, className=NULL, feedback=NULL, feedbackTimeout=NULL, loading_state=NULL, onAnimationEnd=NULL, onClick=NULL, style=NULL) {
    
    props <- list(children=children, id=id, align=align, autoAlign=autoAlign, className=className, feedback=feedback, feedbackTimeout=feedbackTimeout, loading_state=loading_state, onAnimationEnd=onAnimationEnd, onClick=onClick, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Copy',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'autoAlign', 'className', 'feedback', 'feedbackTimeout', 'loading_state', 'onAnimationEnd', 'onClick', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
