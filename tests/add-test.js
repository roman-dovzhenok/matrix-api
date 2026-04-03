import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 5,
  duration: '10s',
};

export default function () {
  const url = 'http://127.0.0.1:5000/api/add';

  const payload = JSON.stringify({
    matrix1: [[1, 2], [3, 4]],
    matrix2: [[5, 6], [7, 8]]
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
    'correct result returned': (r) => r.body.includes('6') && r.body.includes('12'),
  });

  sleep(1);
}