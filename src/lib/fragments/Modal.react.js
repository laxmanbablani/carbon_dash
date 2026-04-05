import React from 'react';
import { Modal as CarbonModal } from '@carbon/react';
import { resolveIcon } from '../utils/resolveIcon';

const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};


const Modal = (props) => {
    const {
        id,
        setProps,
        children,
        className = undefined,
        loading_state,
        style,
        open = null,
        modalHeading = 'Modal Heading',
        primaryButtonText = 'Primary Button',
        secondaryButtonText = 'Secondary Button',
        ...otherProps
    } = props;
    const onRequestClose = (...args) => {
        if (setProps) {
            setProps({
                open: false,
            });
        }
    };

    return (
        <CarbonModal
            data-dash-is-loading={getLoadingState(loading_state)}
            id={id}
            className={className}
            style={style}
            open={open}
            modalHeading={modalHeading}
            primaryButtonText={primaryButtonText}
            secondaryButtonText={secondaryButtonText}
            onRequestClose={onRequestClose}
            {...otherProps}
        >
            {children}
        </CarbonModal>
    );
};

export default Modal;
