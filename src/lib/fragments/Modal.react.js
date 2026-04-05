import React from 'react';
import { Modal as CarbonModal } from '@carbon/react';

const Modal = (props) => {
    const {
        id,
        setProps,
        children,
        className,
        style,
        open,
        modalHeading,
        primaryButtonText,
        secondaryButtonText,
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
