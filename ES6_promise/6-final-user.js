import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  return Promise.allSettled([signUpPromise, uploadPromise]).then((results) => {
    const signUp = {
      status: results[0].status,
      value: results[0].value,
    };
    const upload = {
      status: results[1].status,
      value: results[1].reason.toString(),
    };
    return [signUp, upload];
  });
}
