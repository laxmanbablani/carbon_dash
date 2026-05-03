import React from 'react';
import PropTypes from 'prop-types';
import { Modal as CarbonModal } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Modal = (props) => {
    const { id, children, className = '', style = {}, loading_state, open, ...others } = props;

    const handleRequestClose = () => {
        if (props.setProps) props.setProps({ open: false });
    };

    return (
        <CarbonModal
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            open={open}
            onRequestClose={handleRequestClose}
            {...others}
        >
            {children}
        </CarbonModal>
    );
};

Modal.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Whether the modal is open */
    open: PropTypes.bool,
    /** Modal heading */
    modalHeading: PropTypes.node,
    /** Primary button text */
    primaryButtonText: PropTypes.string,
    /** Secondary button text */
    secondaryButtonText: PropTypes.string,
    /** Whether the modal is a danger modal */
    danger: PropTypes.bool,
    /** Whether the modal should be full width */
    fullWidth: PropTypes.bool,
    /** Whether the modal should be passive */
    passiveModal: PropTypes.bool,
    /** Whether to show the close button */
    preventCloseOnClickOutside: PropTypes.bool,
    /** Size */
    size: PropTypes.oneOf(['xs', 'sm', 'md', 'lg']),
    /** Whether to alert the user */
    alert: PropTypes.bool,
    /** Whether the modal should be displayed with a slider */
    shouldSubmitOnEnter: PropTypes.bool,
    /** Primary button disabled */
    primaryButtonDisabled: PropTypes.bool,
    /** Selector for focus on modal open */
    selectorPrimaryFocus: PropTypes.string,
};

Modal.defaultProps = { open: false, danger: false, fullWidth: false, passiveModal: false, alert: false };

export default Modal;
