﻿namespace Distance_App
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.spdtxt = new System.Windows.Forms.TextBox();
            this.hrtxt = new System.Windows.Forms.TextBox();
            this.Calcbtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(257, 123);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(71, 15);
            this.label1.TabIndex = 0;
            this.label1.Text = "Speed km/h";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(243, 188);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(85, 15);
            this.label2.TabIndex = 1;
            this.label2.Text = "Hours Traveled";
            // 
            // spdtxt
            // 
            this.spdtxt.Location = new System.Drawing.Point(334, 120);
            this.spdtxt.Name = "spdtxt";
            this.spdtxt.Size = new System.Drawing.Size(142, 23);
            this.spdtxt.TabIndex = 2;
            // 
            // hrtxt
            // 
            this.hrtxt.Location = new System.Drawing.Point(334, 185);
            this.hrtxt.Name = "hrtxt";
            this.hrtxt.Size = new System.Drawing.Size(142, 23);
            this.hrtxt.TabIndex = 3;
            // 
            // Calcbtn
            // 
            this.Calcbtn.Location = new System.Drawing.Point(362, 252);
            this.Calcbtn.Name = "Calcbtn";
            this.Calcbtn.Size = new System.Drawing.Size(75, 23);
            this.Calcbtn.TabIndex = 0;
            this.Calcbtn.Text = "Calculate";
            this.Calcbtn.UseVisualStyleBackColor = true;
            this.Calcbtn.Click += new System.EventHandler(this.Calcbtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Calcbtn);
            this.Controls.Add(this.hrtxt);
            this.Controls.Add(this.spdtxt);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Label label1;
        private Label label2;
        private TextBox spdtxt;
        private TextBox hrtxt;
        private Button Calcbtn;
    }
}