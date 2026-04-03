import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 1,
  iterations: 1,
};

export default function () {
  const res = http.get('http://127.0.0.1:5000/health');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'status is ok': (r) => r.body.includes('ok'),
  });

  sleep(1);
}