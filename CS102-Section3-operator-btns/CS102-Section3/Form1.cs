using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace CS102_Section3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void plusbtn_Click(object sender, EventArgs e)
        {
            float num1 = float.Parse(txt1.Text);
            float num2 = float.Parse(txt2.Text);
            float sum = num1 + num2;
            var sumstr = sum.ToString();
            label4.Text = sumstr;

        }

        private void minusbtn_Click(object sender, EventArgs e)
        {
            float num1 = float.Parse(txt1.Text);
            float num2 = float.Parse(txt2.Text);
            float sum = num1 - num2;
            var sumstr = sum.ToString();
            label4.Text = sumstr;
        }

        private void multiplybtn_Click(object sender, EventArgs e)
        {
            float num1 = float.Parse(txt1.Text);
            float num2 = float.Parse(txt2.Text);
            float sum = num1 * num2;
            var sumstr = sum.ToString();
            label4.Text = sumstr;
        }

        private void Dividebtn_Click(object sender, EventArgs e)
        {
            float num1 = float.Parse(txt1.Text);
            float num2 = float.Parse(txt2.Text);
            float sum = num1 / num2;
            var sumstr = sum.ToString();
            label4.Text = sumstr;
        }

    }
}