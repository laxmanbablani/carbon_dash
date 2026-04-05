# AUTO GENERATED FILE - DO NOT EDIT

#' @export
codeSnippet <- function(children=NULL, id=NULL, align=NULL, ariaLabel=NULL, autoAlign=NULL, className=NULL, copyButtonDescription=NULL, copyText=NULL, disabled=NULL, feedback=NULL, feedbackTimeout=NULL, hideCopyButton=NULL, light=NULL, loading_state=NULL, maxCollapsedNumberOfRows=NULL, maxExpandedNumberOfRows=NULL, minCollapsedNumberOfRows=NULL, minExpandedNumberOfRows=NULL, onClick=NULL, showLessText=NULL, showMoreText=NULL, style=NULL, type=NULL, wrapText=NULL) {
    
    props <- list(children=children, id=id, align=align, ariaLabel=ariaLabel, autoAlign=autoAlign, className=className, copyButtonDescription=copyButtonDescription, copyText=copyText, disabled=disabled, feedback=feedback, feedbackTimeout=feedbackTimeout, hideCopyButton=hideCopyButton, light=light, loading_state=loading_state, maxCollapsedNumberOfRows=maxCollapsedNumberOfRows, maxExpandedNumberOfRows=maxExpandedNumberOfRows, minCollapsedNumberOfRows=minCollapsedNumberOfRows, minExpandedNumberOfRows=minExpandedNumberOfRows, onClick=onClick, showLessText=showLessText, showMoreText=showMoreText, style=style, type=type, wrapText=wrapText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CodeSnippet',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'ariaLabel', 'autoAlign', 'className', 'copyButtonDescription', 'copyText', 'disabled', 'feedback', 'feedbackTimeout', 'hideCopyButton', 'light', 'loading_state', 'maxCollapsedNumberOfRows', 'maxExpandedNumberOfRows', 'minCollapsedNumberOfRows', 'minExpandedNumberOfRows', 'onClick', 'showLessText', 'showMoreText', 'style', 'type', 'wrapText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
