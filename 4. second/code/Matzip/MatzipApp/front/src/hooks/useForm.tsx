import {useEffect, useState} from 'react';

interface UserFormProps<T> {
  initialValue: T;
  validate: (values: T) => Record<keyof T, string>;
}

// 여기서 initialValue는 객체임.

function useForm<T>({initialValue, validate}: UserFormProps<T>) {
  const [values, setValues] = useState(initialValue);

  const [touched, setTouched] = useState<Record<string, boolean>>({});

  const [errors, setErrors] = useState<Record<string, string>>({});

  const handleChangeText = (name: keyof T, text: string) => {
    setValues({
      ...values,
      [name]: text,
    });
  };

  const handleBlur = (name: keyof T) => {
    setTouched({
      ...touched,
      [name]: true,
    });
  };

  const getTextInputProps = (name: keyof T) => {
    const value = values[name];
    const onChangeText = (text: string) => handleChangeText(name, text);
    const onBlur = () => handleBlur(name);

    return {value, onChangeText, onBlur};
  };

  useEffect(() => {
    const newErrors = validate(values);
    setErrors(newErrors);
  }, [validate, values]);

  return {values, errors, touched, getTextInputProps};
}

export default useForm;

//Record은 TypeScript의 유틸리티 타입 중 하나로, 특정 타입의 키(key)와 해당 키에 해당하는 값(value)의 타입을 지정할 수 있게 해주는 제네릭 타입입니다. Record<K, T>을 사용하면, 키 타입 K와 값 타입 T를 명시하여 객체를 생성할 수 있습니다.
