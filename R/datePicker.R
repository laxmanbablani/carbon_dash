# AUTO GENERATED FILE - DO NOT EDIT

#' @export
datePicker <- function(children=NULL, id=NULL, allowInput=NULL, appendTo=NULL, className=NULL, closeOnSelect=NULL, dateFormat=NULL, datePickerType=NULL, debounce=NULL, disable=NULL, enable=NULL, inline=NULL, invalid=NULL, invalidText=NULL, light=NULL, loading_state=NULL, locale=NULL, maxDate=NULL, minDate=NULL, n_blur=NULL, n_submit=NULL, nextMonthAriaLabel=NULL, onChange=NULL, onClose=NULL, onOpen=NULL, parseDate=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, prevMonthAriaLabel=NULL, readOnly=NULL, short=NULL, style=NULL, value=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, allowInput=allowInput, appendTo=appendTo, className=className, closeOnSelect=closeOnSelect, dateFormat=dateFormat, datePickerType=datePickerType, debounce=debounce, disable=disable, enable=enable, inline=inline, invalid=invalid, invalidText=invalidText, light=light, loading_state=loading_state, locale=locale, maxDate=maxDate, minDate=minDate, n_blur=n_blur, n_submit=n_submit, nextMonthAriaLabel=nextMonthAriaLabel, onChange=onChange, onClose=onClose, onOpen=onOpen, parseDate=parseDate, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, prevMonthAriaLabel=prevMonthAriaLabel, readOnly=readOnly, short=short, style=style, value=value, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DatePicker',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'allowInput', 'appendTo', 'className', 'closeOnSelect', 'dateFormat', 'datePickerType', 'debounce', 'disable', 'enable', 'inline', 'invalid', 'invalidText', 'light', 'loading_state', 'locale', 'maxDate', 'minDate', 'n_blur', 'n_submit', 'nextMonthAriaLabel', 'onChange', 'onClose', 'onOpen', 'parseDate', 'persisted_props', 'persistence', 'persistence_type', 'prevMonthAriaLabel', 'readOnly', 'short', 'style', 'value', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
