import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((res) => {
      for (const x of res) {
        if (x.status === 'rejected') {
          x.value = `Error: ${x.reason.message}`;
          delete x.reason;
        }
      }
      return res;
    });
}
